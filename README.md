# hostwatch

Auditoria de integridade e permissões de arquivos do host.

## O que faz

Esta ferramenta de **defensiva** contra alvos que voce possui ou tem autorizacao. Auditoria de integridade e permissões de arquivos do host. O codigo e
testavel localmente (sem dependencias de rede para os testes unitarios).

> **Aviso etico:** uso exclusivo para fins educacionais e testes em ambientes
> que voce **possui** ou tem **autorizacao expressa** para auditar. Nunca a
> utilize contra sistemas de terceiros. O autor nao se responsabiliza por uso
> indevido.

## Instalacao

```bash
git clone https://github.com/Diogo-Damasceno/hostwatch.git
cd hostwatch
python3 -m venv .venv && . .venv/bin/activate
pip install -e .
```

## Uso

Detecte binários alterados no seu próprio host.

## Exemplos reais

```bash
$ host-audit /bin /usr/bin
# {'/bin/ls': 'c3d4...'}
```

## Como funciona (resumo)

O modulo principal implementa a logica em funcoes puras e testaveis; a CLI e
apenas a casca de argumentos. Os testes em `tests/` (Python) ou `CoreTest.java`
(Java) cobrem os casos principais e rodam offline.

## O que NAO faz

- Nao executa ataques contra terceiros.
- Nao exfiltra dados.
- Nao substitui uma solucao comercial de seguranca.

## Licenca

MIT — ver `LICENSE`.
