% Definição das cidades e distâncias entre elas
rota(goiania, anapolis, 59).
rota(goiania, rio_verde, 232).
rota(anapolis, brasilia, 154).
rota(rio_verde, brasilia, 437).
rota(rio_verde, luziania, 428).
rota(brasilia, luziania, 60).
rota(luziania, trindade, 236).
rota(trindade, jatai, 314).
rota(jatai, planaltina, 564).
rota(planaltina, goianesia, 275).
rota(goianesia, goiania, 176).

% Definição de uma rota bidirecional
rota_bidirecional(X, Y, D) :- rota(X, Y, D).
rota_bidirecional(X, Y, D) :- rota(Y, X, D).

% Encontrar todas as rotas possíveis de A para B
caminho(A, B, Rota, Distancia) :- caminho(A, B, [A], Rota, Distancia).

caminho(A, B, Visitado, [B|Visitado], Distancia) :-
    rota_bidirecional(A, B, Distancia).

caminho(A, B, Visitado, Rota, Distancia) :-
    rota_bidirecional(A, C, D1),
    C \== B,
    \+ member(C, Visitado),
    caminho(C, B, [C|Visitado], Rota, D2),
    Distancia is D1 + D2.

% Encontrar a melhor rota (menor distância) de A para B
melhor_rota(A, B, Rota, Distancia) :-
    setof([RotaTemp, DistanciaTemp], caminho(A, B, RotaTemp, DistanciaTemp), Rotas),
    Rotas = [[Rota, Distancia]|_].