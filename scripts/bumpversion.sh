#!/bin/bash
# bumpversion.sh [major|minor|patch]
set -euo pipefail

BASE_DIR="$(git rev-parse --show-toplevel)"
ACTION=$1
GREP=grep
SED=sed
INIT_FILE=hue/__init__.py
CHANGELOG_FILE=CHANGELOG.md
PROJECT_NAME=nirantak/hue-api

if [[ "$OSTYPE" =~ "darwin" ]]; then
  # GNU tools required, run `brew install grep sed` for MacOS
  GREP=ggrep
  SED=gsed
fi

CURRENT_VERSION=$($GREP -oP '__version__.*\K\d\.\d\.\d' $BASE_DIR/$INIT_FILE)
ver_arr=(${CURRENT_VERSION//./ })
echo "Current Version: $CURRENT_VERSION"

case $ACTION in
  major)
    ver_arr[0]=$((ver_arr[0]+1))
    ver_arr[1]=0
    ver_arr[2]=0
    ;;

  minor)
    ver_arr[1]=$((ver_arr[1]+1))
    ver_arr[2]=0
    ;;

  patch)
    ver_arr[2]=$((ver_arr[2]+1))
    ;;

  *)
    echo "Invalid Semver Block"
    exit 1
    ;;
esac

NEW_VERSION=$(printf ".%s" "${ver_arr[@]}")
NEW_VERSION=${NEW_VERSION:1}
echo "Current Version: $NEW_VERSION"

set -x
git stash save

$SED -i s/__version__\ =\ \"$CURRENT_VERSION\"/__version__\ =\ \"$NEW_VERSION\"/i $BASE_DIR/$INIT_FILE
$SED -i s@\#\#\ Unreleased.*@\#\#\ \[v$NEW_VERSION\]\(https://github.com/$PROJECT_NAME/releases/tag/v$NEW_VERSION\)\ \($(date '+%Y-%m-%d')\)@i $BASE_DIR/$CHANGELOG_FILE

git add $BASE_DIR/$INIT_FILE $BASE_DIR/$CHANGELOG_FILE
git --no-pager diff --staged
git commit -m "Bump version: $CURRENT_VERSION → $NEW_VERSION"
git tag v$NEW_VERSION -m "Bump version: $CURRENT_VERSION → $NEW_VERSION"
git stash pop || true
