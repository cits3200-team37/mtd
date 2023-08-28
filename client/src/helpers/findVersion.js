/**
 * Takes in the window element from the 'website' and tests it to see if its an app or not
 * @param {window} window element 
 * @returns {boolean} true if electron, false if not
 */

export default function findVersion(window) {
    if ((window && window.process && window.process.type == 'renderer') == true) return true;
    else return false;
}