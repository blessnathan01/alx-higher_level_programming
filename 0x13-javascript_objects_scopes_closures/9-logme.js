#!/usr/bin/node
// a function that prints the number of arguments already printed and the new argument value
function * generator () {
  let idx = 0;
  while (true) {
    yield idx++;
  }
}
const gen = generator();
exports.logMe = function (item) {
  console.log(gen.next().value + ': ' + item);
};
