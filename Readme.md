# INSTRUKCJA DZIAŁANIA RADARU

- Po podłączeniu i zasileniu, mikrokontroler rozpoczyna komunikacje z komputerem poprzez kabel USB
- Na początku pozycja serwomechanizmu jest ustawiana na 1°
- Następnie mikrokontroler, używając kabla oznaczonego jako "TRIG„ wysyła 10 μs sygnał do sensora ultradźwiękowego, który wysyła pojedynczą falę ultradźwiękową o częstotliwości 40 000 Hz
- Sensor po otrzymaniu fali powrotnej, ze wzoru **dystans = prędkość dźwięku × czas od wysłania do powrotu fali** (s=vt) oblicza odległość do przedmiotu i razem z obecnym kątem ustawienia serwomechanizmu, wysyła ją kablem kablem do komputera
- Mikrokontroler po każdym pomiarze odległości ustawia serwomechanizm na jeden stopień dalej i wykonuje kolejny pomiar
- Cały powyższy proces jest wykonywany w pętli, tak długo jak radar jest podłączony do komputera i ma zasilanie

#
<Center>Pętla programu:</Center>

```mermaid
graph LR
A(Do pozycji serwa dodawany jest 1 stopień) --> B(Czujnik wykonuje pomiar)
B --> C(Pomiar wysyłany jest do komputera)
C --> A
```

#
>![](https://raw.githubusercontent.com/FabianOlczakk/FizykaRadar/master/.md/slImage%20(1).png)
>![](https://raw.githubusercontent.com/FabianOlczakk/FizykaRadar/master/.md/slImage%20(2).png)

#
# INSTRUKCJA DZIAŁANIA PROGRAMU
- Po odpaleniu programu, ten łączy się z radarem, poprzez kabel USB 
- Program odczytuje dane z mikrokontrolera
- Następnie jest obliczana pozycja x oraz y punktu na radarze: 
	>**x = dystans × cos(kąt ustawienia serwomechanizmu)**
	>**y = dystans × sin(kąt ustawienia serwomechanizmu)**
- Program wyświetla punkty w obliczonych pozycjach 

