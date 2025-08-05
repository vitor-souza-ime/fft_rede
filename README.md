# FFT Rede Elétrica - Análise Harmônica em Python

Este repositório contém um script em Python para análise harmônica de sinais senoidais típicos de sistemas elétricos de potência. O código utiliza a Transformada Rápida de Fourier (FFT) para detectar e quantificar harmônicos em uma forma de onda composta, além de calcular a Distorção Harmônica Total (THD).

---

## Arquivo principal

- `main.py`: Código fonte para geração do sinal, aplicação da FFT, detecção dos harmônicos até o 50º, cálculo do THD e plotagem dos resultados.

---

## Funcionalidades

- Geração de sinal senoidal com fundamental de 60 Hz e múltiplos harmônicos.
- Aplicação de janela de Hanning para minimizar vazamento espectral.
- Cálculo da FFT e extração do espectro de frequência.
- Identificação dos harmônicos próximos a múltiplos inteiros da fundamental.
- Cálculo da Distorção Harmônica Total (THD).
- Visualização gráfica do sinal no domínio do tempo e do espectro harmônico.

---

## Requisitos

- Python 3.x
- Bibliotecas:
  - numpy
  - matplotlib
  - scipy

Instale as bibliotecas necessárias com:

```bash
pip install numpy matplotlib scipy
````

---

## Uso

Execute o script principal:

```bash
python main.py
```

O programa exibirá:

* Gráfico do sinal no domínio do tempo (amostra dos primeiros instantes).
* Gráfico do espectro harmônico até o 50º harmônico.
* Valores numéricos dos harmônicos detectados e a THD calculada.

---

## Link do Repositório

[https://github.com/vitor-souza-ime/fft\_rede](https://github.com/vitor-souza-ime/fft_rede)

---

## Exemplo de saída

```
THD: 26.68%

Harmônicos detectados (Hz) e Magnitudes:
H1: 60 Hz - Magnitude: 1.0000
H2: 120 Hz - Magnitude: 0.3000
H3: 180 Hz - Magnitude: 0.2000
H4: 240 Hz - Magnitude: 0.1000
H5: 300 Hz - Magnitude: 0.0500
...
```

---



