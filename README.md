# host-audit

Auditoria de integridade e permissões de arquivos do host.

> **Aviso etico:** ferramenta exclusiva para fins educacionais e testes em
> ambientes que voce possui ou tem autorizacao para auditar. Categoria:
> Defensiva. Nunca a use contra terceiros.

## Instalacao

```bash
git clone https://github.com/Diogo-Damasceno/host-audit.git
cd host-audit
python3 -m venv .venv && . .venv/bin/activate
pip install -e .
```

## Uso

Detecte binários alterados no seu próprio host.

Exemplos reais:

```
  $ host-audit /bin /usr/bin
  {'/bin/ls': 'c3d4...'}```

## Arquitetura

`src/host_audit/core.py` tem a logica pura (funcoes testaveis); `cli.py` e a
casca de argumentos. Testes em `tests/` cobrem os casos principais.
