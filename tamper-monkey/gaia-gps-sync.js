// ==UserScript==
// @name         Gaia GPS Google Maps sync
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Adds a button
// @author       You
// @match        https://www.gaiagps.com/map/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=gaiagps.com
// @grant        none
// ==/UserScript==


/**
 * Convert a template string into HTML DOM nodes
 * 
 * https://gomakethings.com/converting-a-string-into-markup-with-vanilla-js/
 * 
 * @param  {String} str The template string
 * @return {Node}       The template HTML
 */
 const stringToHTML = function (str) {
	var parser = new DOMParser();
	var doc = parser.parseFromString(str, 'text/html');
	return doc.body;
};

/**
 * @callback onLoadHTMLCallback
 * @param {Element} el 
 * @returns 
 */


/**
 * https://stackoverflow.com/a/40135630
 * @param {onLoadHTMLCallback} callback 
 * @returns 
 */
const onLoadHTML = function (callback) {
    return new MutationObserver( mutation => {
        if (!mutation.addedNodes) return;

        console.log("has mutations")
        mutation.addedNodes.forEach(callback);
    });
};


/**
 * 
 * @param {Element} callback 
 * @returns 
 */
const addCustomItems = function (el) {
    if (!(el instanceof Element)) return;
    console.log('wat', el);

    let elMuiDividerLast = el.querySelectorAll('ul.MuiList-root.MuiList-padding').pop();
    if (!elMuiDividerLast) return;

    console.log(elMuiDividerLast)

    // let elCustomItems = stringToHTML(/* HTML */`
    //     <ul class="MuiList-root MuiList-padding" style="padding-top: 0px;">
    //         <li class="">
    //             <div class="MuiButtonBase-root MuiListItem-root jss39 MuiListItem-button"
    //                     tabindex="0"
    //                     role="button"
    //                     aria-disabled="false"
    //                     aria-label="Create Waypoint">
    //                 <div class="MuiListItemIcon-root"></div>
    //                 <div class="MuiListItemText-root">
    //                 <span class="MuiTypography-root MuiListItemText-primary MuiTypography-body1 MuiTypography-displayBlock">
    //                     Google
    //                 </span>
    //             </div>
    //         </li>
    //     </ul>
    // `);

    // elMuiDividerLast.after(elCustomItems);
};

(function() {
    'use strict';

    // loc=14.0/-85.9407/44.7464

    onLoadHTML(el => {
        if (!el.matches('.MuiDivider-root')) return;

        addCustomItems(el);
    });
    console.log('huh?');
})();
