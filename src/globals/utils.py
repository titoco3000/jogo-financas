def lerp(a, b, x: float):
    """Interpolação linear para valores escalares ou vetoriais"""
    if hasattr(a, "__len__"):
        if len(a) != len(b):
            raise Exception(
                f"Não é possível fazer lerp em vetores de tamanhos diferentes ({len(a)} e {len(b)})"
            )
        return [lerp(a, b, x) for a, b in zip(a, b)]
    else:
        return (1.0 - x) * a + x * b


def animation_lerp(keyframes, current_time):

    timeline = []
    t = 0
    for value, dt in keyframes:
        timeline.append((value, t))
        t += dt

    # Se o tempo for antes do primeiro keyframe, retorna o primeiro valor
    if current_time <= timeline[0][1]:
        return timeline[0][0]

    # Se o tempo for depois do último keyframe, retorna o último valor
    if current_time >= timeline[-1][1]:
        return timeline[-1][0]

    # Procurar o intervalo certo
    for i in range(len(timeline) - 1):
        a_val, a_time = timeline[i]
        b_val, b_time = timeline[i + 1]

        if a_time <= current_time <= b_time:
            # Calcular o fator de interpolação
            t = (current_time - a_time) / (b_time - a_time)
            return lerp(a_val, b_val, t)

    raise Exception("Tempo fora dos keyframes.")


# exemplo de uso
# triangulo = [
#     ([0,0], 0),
#     ([0,10], 3),
#     ([10,10], 10)
# ]
# animation_lerp(triangulo,1) # retorna lerp(triangulo[0], triangulo[1], 1/3)
# animation_lerp(triangulo,3) # retorna lerp(triangulo[0], triangulo[1], 3/3)
# animation_lerp(triangulo,5) # retorna lerp(triangulo[1], triangulo[2], 2/7)
