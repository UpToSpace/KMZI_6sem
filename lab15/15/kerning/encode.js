const fs = require("fs");
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const dom = new JSDOM(fs.readFileSync("file.html").toString());
const message = 'valeria';


function textToBinary(str = '') {
    let res = '';
    res = str.split('').map(char => {
        return char.charCodeAt(0).toString(2);
    }).join('');
    return res;
};


const div = dom.window.document.getElementById('container');
div.innerHTML = div.textContent.split('').map(letter => 
    letter.trim() === '' ? ' ' : `<span style="margin-left: 0.5px;">${letter}</span>`
).join("");
const spans = dom.window.document.getElementsByTagName('span');
bits = textToBinary(message);
for (i = 0; i < bits.length; i++) {
    if (bits[i] === '0') {
        spans[i].style.marginLeft = '0px';
    }
    else {
        spans[i].style.marginLeft = '1px';
    }
};

fs.writeFile('encoded.html', dom.serialize(), () => {});
