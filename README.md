[PYTHON_BADGE]: https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python&logoColor=lightskyblue
[DJANGO_BADGE]: https://img.shields.io/badge/Django-6.1.1-092E20?style=for-the-badge&logo=django&logoColor=white
[DRF_BADGE]: https://img.shields.io/badge/DRF-3.18.1-a30000?style=for-the-badge&logo=django&logoColor=white
[PRS_BADGE]: https://img.shields.io/badge/PRs-welcome-green?style=for-the-badge

<h1 align="center" style="font-weight: bold;">API Cidades 💻</h1>

![python][PYTHON_BADGE]
![django][DJANGO_BADGE]
![drf][DRF_BADGE]

<details open="open">
<summary>Sumário</summary>

- [🚀 Getting started](#started)
  - [Prerequisites](#prerequisites)
  - [Cloning](#cloning)
  - [Starting](#starting)
- [📍 API Endpoints](#routes)
  - [GET /api/cities/](#get-cities-list)
  - [GET /api/cities/{id}/](#get-cities-detail)
- [🤝 Collaborators](#colab)
- [📫 Contribute](#contribute)
- [Informações adicionais](#informações-adicionais)

</details>

<h2 id="started">🚀 Getting started</h2>

How to run the project locally.

<h3 id="prerequisites">Prerequisites</h3>

| Package | Verion | In Project |
|---|---|---|
| Django | 6.1.1 | Framework web; ORM, admin, migrations e `manage.py` |
| djangorestframework | 3.18.1 | API REST (`ViewSet`, `DefaultRouter`, serializers, `APITestCase`) |

<h3 id="cloning">Cloning</h3>

```bash
git clone https://github.com/eduBortotowski/api_cidades.git
cd api_cidades
```

<h3 id="starting">Starting</h3>

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

URL running: `http://127.0.0.1:8000/`.


<h2 id="routes">📍 API Endpoints</h2>

| Route | Description |
|---|---|
| <kbd>/api/cities/</kbd> | Returns list of Cities — [details](#get-cities-list) |
| <kbd>/api/cities/{id}/</kbd> | Returns details of city — [details](#get-cities-detail) |

- <h3 id="get-cities-list">GET /api/cities/</h3>

**RESPONSE**

```json
[
  {
    "id": 1,
    "name": "Olinda"
  },
  {
    "id": 2,
    "name": "Recife"
  }
]
```

<h3 id="get-cities-detail">GET /api/cities/{id}/</h3>

**RESPONSE**

```json
{
  "id": 1,
  "name": "Recife"
}
```

<h2 id="colab">🤝 Collaborators</h2>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/eduBortotowski" title="Perfil de Eduardo Bortowski de Sousa no GitHub">
        <img src="https://github.com/eduBortotowski.png" width="100" alt="Foto de Eduardo Bortowski de Sousa no GitHub"/><br>
        <sub>
          <b>Eduardo Bortowski de Sousa</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="contribute">📝 License</h2>

This API was created for study purposes. No commercial license.
