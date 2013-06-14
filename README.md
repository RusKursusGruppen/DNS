DNS
===
Den Ny' Sangbog

Nyt og simplere system til at skabe årets rusturs sangebog.

Målet er at lave et system i et enkelt sprog (dvs. 2! LaTeX og Python) som er
nemmere at vedligeholde for de næste. Så kan vi også slippe for chord! Fy for
den lede!

BRUG
---
Hver sang er en .tex fil i "sange" mappen.
Eksempel på sang fil:

    \sang{Blev på DIKU baby}
    {DIKUrevy 2011}
    {he Offspring - Pretty Fly}
    {
    \omkv{Bliv på DIKU baby (uh huh, uh huh)
    bliv på DIKU baby (uh huh, uh huh)........}

    Det handler ikke om at, tage DIKUs fag
    Kurserne er nemme, at bestå er ingen sag.......

    \kom{Så skal i huske at være sjove!}
    }

 Filnavnet er ligemeget, men det er flinkt hvis man giver den et sigende navn,
 f.eks. titlen på sangen, uden spaces? ;)

 Der kan indsættes arbitrær \TeX kode i alle sange. Der er ingen garanti for
 hvordan systemet håndtere skidtet!