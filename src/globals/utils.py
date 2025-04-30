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
