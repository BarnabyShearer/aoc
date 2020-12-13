from aoc20191221a import springbot


def aoc(data):
    return springbot(
        data,
        """NOT B J
NOT C T
OR T J
AND H J
AND D J
NOT A T
OR T J
RUN
""",
    )
