let menu = [{
        "label": "Home",
        "path": "home"
    },
    {
        "label": "Technical Skills",
        "path": "technical-skills"
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

    a.href = window.location.origin + '/#' + path;
    a.innerText = label;
    a.addEventListener('click', function () {
        let sections = document.querySelectorAll("section[id]");
        sections.forEach(section => {
            let section_id = section.getAttribute("id");
            if (section_id === path) {
                document.querySelector(".nav-container a[href*=" + section_id + "]").style.color = '#f42735';
            } else {
                document.querySelector(".nav-container a[href*=" + section_id + "]").style.color = '#ffffff';
            }
        });
    });
    li.append(a);
    ul.append(li);
}
nav.append(ul);
navContainer.append(nav);