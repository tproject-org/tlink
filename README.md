<br/>
<p align="center">
  <a href="https://github.com/tproject-org/tlink">
    <img src="https://raw.githubusercontent.com/tproject-org/tlink/main/brands/logo_square.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TLINK</h3>

  <p align="center">
    A simple url shorter
    <br/>
    <br/>
    <a href="https://github.com/tproject-org/tlink"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/tproject-org/tlink">View Demo</a>
    .
    <a href="https://github.com/tproject-org/tlink/issues">Report Bug</a>
    .
    <a href="https://github.com/tproject-org/tlink/issues">Request Feature</a>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

ABOUT TODO

## Built With



* [Django](https://djangoproject.com)
* [Django Rest Framework](https://django-rest-framework.org)
* [Emblems](https://apps.gnome.org/app/org.gnome.design.Emblem/)

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

You need `git`, `python` and `wget` or  `curl` (`pacman -S git python base-devel`)

### Installation

#### Rapid install

Simply run `setup.sh` (review it before :D)

```sh
wget https://github.com/tproject-org/tlink/raw/main/setup.sh
chmod +x setup.sh
./setup.sh
```

#### Long install

1. Create a virtualenv and activate the virtualenv

```sh
virtualenv tlink-env
source tlink-env/bin/activate
```

2. Clone the repo

```sh
git clone https://github.com/tproject-org/tlink.git
```

3. Install requirements

```sh
pip install -R requirements.txt
```

3. Run migration and create superuser

```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

4. Open your browser at [127.0.0.1:8000](http://127.0.0.1:8000)



## Usage

Go to your Tlink instance and log in. After that, you can create short url. If you write nothing in short url, it will generate a short url for you.

## Roadmap

See the [open issues](https://github.com/tproject-org/tlink/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/tproject-org/tlink/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/tproject-org/tlink/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/tproject-org/tlink/blob/main/LICENSE.md) for more information.

## Authors

* **Itotutona** - *Ingenieer* - [Itotutona](https://github.com/itotutona) - *Creator of Tproject*

