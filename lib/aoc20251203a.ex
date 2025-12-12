defmodule Aoc20251203a do
  def parse(line), do: String.split(line, "", trim: true) |> Enum.map(&String.to_integer/1)

  def calc(_, {total, 0}), do: {total, 0}

  def calc(battries, {total, digits}) do
    max =
      Enum.slice(battries, 0, length(battries) - digits + 1)
      |> Enum.max()

    max_index = Enum.find_index(battries, fn x -> x == max end)

    rest =
      calc(Enum.slice(battries, (max_index + 1)..length(battries)), {0, digits - 1})
      |> elem(0)

    {total + max * trunc(:math.pow(10, digits - 1)) + rest, digits}
  end

  def call(input) do
    Enum.map(input, &parse/1)
    |> Enum.reduce({0, 2}, &calc/2)
    |> elem(0)
  end
end
