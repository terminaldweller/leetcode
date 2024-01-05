#!/usr/bin/env node
"use strict";

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  var resArr = new Array();
  for (var i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      resArr[i].push(arr[i]);
    }
  }
  return resArr;
};
