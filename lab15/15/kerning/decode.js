const fs = require("fs");
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const dom = new JSDOM(fs.readFileSync('encoded.html').toString());
const spans = dom.window.document.getElementById('container').getElementsByTagName('span');


function binaryToText(bits) {
    let bytes = bits.match(/.{1,7}/g);
    bytes = bytes.map(elem => parseInt(elem, 2));
    bytes = bytes.map(elem => String.fromCharCode(elem));
    let text = bytes.join('');
    return text;
}


bits = '';
for (i = 0; i < spans.length; i++) {
    if (spans[i].style.marginLeft === '0px') {
        bits += '0';
    }
    else if (spans[i].style.marginLeft === '1px') {
        bits += '1';
    }
    else {
        break;
    }
}
console.log(`Decoded message: ${binaryToText(bits)}`);
