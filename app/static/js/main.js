let menu = [{
		"label": "Home",
		"path": "#home",
		"selected": false
	},
	{
		"label": "Technical Skills",
		"path": "#technical-skills",
		"selected": false
	},
	{
		"label": "Projects",
		"path": "#projects",
		"selected": false
	},
	{
		"label": "Blogs",
		"path": "#blogs",
		"selected": false
	},
	{
		"label": "About Me",
		"path": "#about-me",
		"selected": false
	}
]

let activateMenu;
function selectMenu(menu) {
	 document.getElementById(menu).style.color = "#f42735";
	 if(activateMenu != null) {
	   document.getElementById(activateMenu).style.color = "#fff";
	 }
	 activateMenu = menu;
}

let navContainer = document.querySelector('.desktop-nav-container');
let nav = document.createElement('nav');
let ul = document.createElement('ul');
for(let i=0; i<menu.length; i++) {
	let li = document.createElement('li');
	let a = document.createElement('a');
	a.href = menu[i].path;
	a.innerText = menu[i].label;
	a.setAttribute('id', menu[i].label);
	a.addEventListener('click', function () {
		selectMenu(menu[i].label);
	});
	li.append(a);
	ul.append(li);
}
nav.append(ul);
navContainer.append(nav);
