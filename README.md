<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/Insiares/scraper/workflow.yml)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Insiares/scraper">
  </a>

<h3 align="center">Quote Scraper</h3>

  <p align="center">
    A simple scraper tool crawling the quotes to scrape website
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![App Screen Shot][product-screenshot]

A scraping service built on Scrapy, served with Flask, and deployed using Acorn.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-shield]][Python-url]
* [![flask][flask-shield]][flask-url]
* [![mongo][mongo-shield]][mongo-url]
* ![Static Badge](https://img.shields.io/badge/Acorn-orange?style=flat&color=orange&link=https%3A%2F%2Facorn.io%2F)
* ![Static Badge](https://img.shields.io/badge/Scrapy-brightgreen?style=flat-square&link=https%3A%2F%2Fscrapy.org%2F)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
--
This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/Insiares/scraper.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Create our spider
- [x] mount mongodb
    - [x] Implement an item pipeline to populate our dabatabase from the spider findings
- [x] Build an API on top of your system
    - [x] Present it in a nice html/css 
- [x] run unit tests
- [x] implement logging
- [x] Write dockerfile
- [x] deploy on acorn
    - [x] CI with acorn/dockerhub : add credential to GH actions and acorn logic to build and push to dockerio
    - [x] attempt to CD with acorn autoupdate
- [ ] security test
- [ ] documentation


See the [open issues](https://github.com/Insiares/scraper/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Insiares/scraper.svg?style=for-the-badge
[contributors-url]: https://github.com/Insiares/scraper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Insiares/scraper.svg?style=for-the-badge
[forks-url]: https://github.com/Insiares/scraper/network/members
[stars-shield]: https://img.shields.io/github/stars/Insiares/scraper.svg?style=for-the-badge
[stars-url]: https://github.com/Insiares/scraper/stargazers
[issues-shield]: https://img.shields.io/github/issues/Insiares/scraper.svg?style=for-the-badge
[issues-url]: https://github.com/Insiares/scraper/issues
[license-shield]: https://img.shields.io/github/license/Insiares/scraper.svg?style=for-the-badge
[license-url]: https://github.com/Insiares/scraper/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: static/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python-shield]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]:https://www.python.org/
[Streamlit-shield]:https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[Streamlit-url]:https://streamlit.io/
[flask-shield]:https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[mysql-shield]:https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white
[scikit-shield]:https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[NumPy]:https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[mongo-shield]:https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white
[mongo-url]:www.mongodb.com
