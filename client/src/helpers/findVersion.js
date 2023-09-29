/**
 * Takes in the user agent element from the 'website' and tests it to see if its an app or not
 * @param {navigator.userAgent} agent element
 * @returns {boolean} true if electron, false if not
 */

export default function findVersion(userAgent) {
  if (userAgent.indexOf("Electron") > -1)
    return true;
  else return false;
}
