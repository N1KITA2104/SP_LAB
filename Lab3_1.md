# 51. (kk|ɛ)((kg)+g)*g(gk)*

- e0 = ε
- e1 = kk
- e2 = kg
- e3 = g
- e4 = g
- e5 = gk
  
<hr>

- S0 -> ε
- S1 -> kk
- S2 -> kg
- S3 -> g
- S4 -> g
- S5 -> gk

<hr>

### Далі обробимо складніші конструкції:

kk | ɛ:
- S6 -> S0 | S1
- S0 -> ε
- S1 -> kk

(kg)+ :
- S7 -> S2
- S2 -> kg
- S2 -> kgS7

(kg)+g:
- S7 -> S2
- S2 -> kgS3
- S2 -> kgS7
- S3 -> g

((kg)+g)*:
- S8 -> S7 | ɛ
- S7 -> S2
- S2 -> kgS3
- S2 -> kgS7
- S3 -> g
- S3 -> gS8

(kk|ɛ)((kg)+g)*:
- S6 -> S0 | S1
- S0 -> S8
- S1 -> kkS8
- S8 -> S7 | ɛ
- S7 -> S2
- S2 -> kgS3
- S2 -> kgS7
- S3 -> g
- S3 -> gS8

(kk|ɛ)((kg)+g)*g:
- S6 -> S0 | S1
- S0 -> S8
- S1 -> kkS8
- S8 -> S7 | S4
- S7 -> S2
- S2 -> kgS3
- S2 -> kgS7
- S3 -> gS4
- S3 -> gS8
- S4 -> g

(gk)*:
- S9 -> S5 | ɛ
- S5 -> gk
- S5 -> gkS9

(kk|ɛ)((kg)+g)*g(gk)*:
- S6 -> S0 | S1
- S0 -> S8
- S1 -> kkS8
- S8 -> S7 | S4
- S7 -> S2
- S2 -> kgS3
- S2 -> kgS7
- S3 -> gS4
- S3 -> gS8
- S4 -> gS9
- S9 -> S5 | ɛ
- S5 -> gk
- S5 -> gkS9
