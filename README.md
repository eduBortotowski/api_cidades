# api_cidades

![GitHub repo size](https://img.shields.io/github/repo-size/eduBortotowski/api_cidades?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/eduBortotowski/api_cidades?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/eduBortotowski/api_cidades?style=for-the-badge)
![GitHub open issues](https://img.shields.io/github/issues/eduBortotowski/api_cidades?style=for-the-badge)
![GitHub open pull requests](https://img.shields.io/github/issues-pr/eduBortotowski/api_cidades?style=for-the-badge)

> ⚠️ Não identificado no código — confirmar com o time. Nenhuma imagem de capa no repositório.

> API REST somente leitura de cidades, em Django e Django REST Framework.
> Expõe `CityViewSet` (`ReadOnlyModelViewSet`): listar e detalhar o model `City` (`id`, `name`).
> Prefixo `api/`; banco SQLite (`db.sqlite3`). Sem create/update/delete.

## Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:

- [x] `GET /api/cities/` (`CityViewSet` + testes em `cities/tests.py`)
- [x] `GET /api/cities/{id}/` (`ReadOnlyModelViewSet.retrieve`; sem teste)
- [x] Model `City` (`name`, `Meta.ordering = ["name"]`) e serializer (`id`, `name`)
- [x] Migration inicial (`cities/migrations/0001_initial.py`) e fixture `cities/fixtures/cities.json`
- [ ] Teste de detalhe `GET /api/cities/{id}/`
- [ ] OpenAPI/Swagger
- [ ] Paginação (`REST_FRAMEWORK` ausente em `setup/settings.py`)
- [ ] Autenticação/autorização customizada
- [ ] Docker / Compose
- [ ] Registro de `City` no admin (`cities/admin.py` vazio)

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python: versão **não pinada** em `requirements.txt` nem em manifesto.

  > ⚠️ Não identificado no código — confirmar com o time. (`CLAUDE.MD` cita Python 3.12+; isso não está pinado.)

- Pacotes em `requirements.txt`:

  | Pacote | Versão |
  |---|---|
  | Django | 6.1.1 |
  | djangorestframework | 3.18.1 |
  | asgiref | 3.12.1 |
  | sqlparse | 0.6.0 |

- Sistema operacional:

  > ⚠️ Não identificado no código — confirmar com o time.

- Variável de ambiente referenciada no código: `DJANGO_SETTINGS_MODULE` (default `setup.settings` em `manage.py`, `setup/wsgi.py`, `setup/asgi.py`). Não há `.env` nem `.env.example`. Banco: SQLite (`django.db.backends.sqlite3`, arquivo `db.sqlite3`, ignorado no `.gitignore`).

## 🚀 Instalando api_cidades

Para instalar o api_cidades, siga estas etapas:

```bash
pip install -r requirements.txt
```

Há migration inicial em `cities/migrations/0001_initial.py`. Aplicá-la com `python manage.py migrate` é o fluxo padrão do Django; o comando **não está scriptado** no projeto.

## ☕ Usando api_cidades

Para usar o api_cidades, siga estas etapas (comandos citados em `CLAUDE.MD`):

```bash
python manage.py check
python manage.py test
```

Servidor HTTP local, host e porta:

> ⚠️ Não identificado no código — confirmar com o time. Não há Makefile, script de start nem `runserver` documentado no repositório.

Dados de exemplo: fixture `cities/fixtures/cities.json` (`model`: `cities.city`, campo `name`).

### Endpoints

Prefixo `api/` (`setup/urls.py`). Recurso `cities` no `DefaultRouter` (`cities/urls.py`). ViewSet somente leitura (`cities/views.py`).

| Método | Rota | Descrição | Auth |
|---|---|---|---|
| GET | `/api/cities/` | Lista cidades | nenhuma configuração explícita |
| GET | `/api/cities/{id}/` | Detalhe de uma cidade | nenhuma configuração explícita |
| — | `/admin/` | Admin Django | auth padrão do Django |

`City` não está registrado em `cities/admin.py`. Sem paginação, permissões ou autenticação customizadas no settings.

### Modelo `City`

| Campo | Tipo | Notas |
|---|---|---|
| `id` | `BigAutoField` | PK (Django) |
| `name` | `CharField(max_length=100)` | — |

`Meta.ordering = ["name"]`. Sem relações com outros models.

### Testes

Arquivo: `cities/tests.py` (`APITestCase`).

| Caso | O que valida |
|---|---|
| `test_list_empty_returns_200` | `GET /api/cities/` → 200 e `[]` |
| `test_list_with_items_returns_200` | lista com itens, 200, ordem `Olinda`, `Recife` |

Não há teste de detalhe (`/api/cities/{id}/`).

## 📫 Contribuindo para api_cidades

> ⚠️ Não identificado no código — confirmar com o time. Não há `CONTRIBUTING.md` nem fluxo de contribuição definido no repositório.

Documentação genérica do GitHub (não é deste projeto): [como criar uma solicitação pull](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

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

Fonte: `git log` (`Eduardo Bortowski de Sousa`) e remote `git@github.com:eduBortotowski/api_cidades.git`.

## 😄 Seja um dos contribuidores

> ⚠️ Não identificado no código — confirmar com o time. Arquivo `CONTRIBUTING.md` inexistente.

## 📝 Licença

> ⚠️ Não identificado no código — confirmar com o time. Não há `LICENSE` nem `LICENSE.md`.
