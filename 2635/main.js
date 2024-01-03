#!/usr/bin/env node
"use strict";

/**
 *  * @param {number[]} arr
 *  * @param {Function} fn
 *  * @return {number[]}
 *  */
var map = function (arr, fn) {
  var resArr = new Array();
  var i = 0;
  arr.forEach((element) => {
    resArr.push(fn(element, i));
    i++;
  });
  return resArr;
};
