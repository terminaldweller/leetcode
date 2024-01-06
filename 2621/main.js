#!/usr/bin/env node
"use strict";

/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
  await new Promise((resolve) => setTimeout(resolve, millis));
}

/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
