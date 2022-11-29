#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const match = list.filter(element => element === searchElement);
  return match.length;
};
