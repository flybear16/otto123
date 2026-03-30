#!/bin/bash

BASE_URL="https://flybear16.github.io/otto123"
PAGES=(
  "/#/"
  "/#/business/"
  "/#/business/school/"
  "/#/business/school/01-overview"
  "/#/business/school/02-model"
  "/#/business/school/03-curriculum"
  "/#/business/school/04-negotiation"
  "/#/business/school/05-operations"
  "/#/business/school/06-finance"
  "/#/business/school/07-risk"
  "/#/business/school/08-appendix"
  "/#/business/daycare/"
  "/#/product/"
  "/#/operations/"
  "/overview/vision"n)

echo "开始截图..."
for page in "${PAGES[@]}; do
  filename=$(echo $page | sed 's/[#\/]//g' | sed 's/^\///')
  [ -z "$filename" ] && filename="home"
  echo "截图: $page -> screenshots/${filename}.png"
done
echo "完成"
