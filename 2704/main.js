#!/usr/bin/env node
"use strict";

var expect = function (val) {
  var object = {
    toBe: function (except) {
      if (except === val) {
        return true;
      } else {
        throw "Not Equal";
      }
    },
    notToBe: function (except) {
      if (except !== val) {
        return true;
      } else {
        throw "Equal";
      }
    },
  };
  return object;
};

console.log(expect(5).toBe(5)); // true
console.log(expect(5).notToBe(5)); // throws "Equal"
