let menu = [{
        "label": "Home",
        "path": "home"
    },
    {
        "label": "Tech Skills",
        "path": "tech-skills"
    },
    {
        "label": "Projects",
        "path": "projects"
    },
    {
        "label": "Blogs",
        "path": "blogs"
    },
    {
        "label": "About Me",
        "path": "about-me"
    }
]

let navContainer = document.querySelector('.nav-container');
let nav = document.createElement('nav');
let ul = document.createElement('ul');

for (let i = 0; i < menu.length; i++) {
    let li = document.createElement('li');
    let a = document.createElement('a');
    let label = menu[i].label;
    let path = menu[i].path;
    let url = new URL(window.location.href);

    if(url.hash.includes(path)) {
        a.style.color = '#f42735';
    }
    a.href = window.location.origin + '/#' + path;
    a.innerText = label;
    a.addEventListener('click', function () {
        let sections = document.querySelectorAll("section[id]");
        sections.forEach(section => {
            let section_id = section.getAttribute("id");
            let item = document.querySelector(".nav-container a[href*=" + section_id + "]");
            if (section_id === path) {
                item.style.color = '#f42735';
            } else {
                item.style.color = '#ffffff';
            }
        });
    });
    li.append(a);
    ul.append(li);
}
nav.append(ul);
navContainer.append(nav);