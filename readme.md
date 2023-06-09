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

[![LinkedIn][linkedin-shield]][linkedin-url]




<h3 align="center">eCore Selenium Python Code Challenge</h3>

  <p align="center">
    POM, Python and Selenium automation test. 
    <br />
    <a href="https://github.com/maxoliverbr/eCoreSeleniumPython"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/maxoliverbr/eCoreSeleniumPython">View Demo</a>
    ·
    <a href="https://github.com/maxoliverbr/eCoreSeleniumPython/issues">Report Bug</a>
    ·
    <a href="https://github.com/maxoliverbr/eCoreSeleniumPython/issues">Request Feature</a>
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

Code challenge by Daniel Guimarães for eCore Senior QA Automation
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Selenium][Selenium]][Selenium-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This app was developed using Page Object Model pattern (POM) to automate access via login of webapp 
and validate functionality and information presented to the user using Python, Selenium and Chrome.

There are 3 pages in this app:
* Login
* Account
* Invoice

### Prerequisites

In order to test this application it is required:
* Python 3.10.11
* Selenium 4.9
* Pytest 7.3.1
* Chrome Latest Version


### Installation

1. Clone the repo
   ```sh
   gh repo clone maxoliverbr/eCoreSeleniumPython
   ```
2. Install packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run tests with pytest
   ```sh
   pytest -v tests
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- ROADMAP -->
## Roadmap

- [ ] Fix 2 known issues
- [ ] Improve code for other browsers

See the [open issues](https://github.com/maxoliverbr/eCoreSeleniumPython/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Private eCore License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Max Oliver - max.oliver@cintrax.com.br

Project Link: [https://github.com/maxoliverbr/eCoreSeleniumPython](https://github.com/maxoliverbr/eCoreSeleniumPython)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/maxoliver
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org
[Selenium]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/
