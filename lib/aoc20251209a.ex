defmodule Aoc20251209a do
  def parse(line),
    do: String.split(line, ",") |> Enum.map(&String.to_integer/1) |> (fn [x, y] -> {x, y} end).()

  def area([{x1, y1}, {x2, y2}]),
    do: (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

  def call(input) do
    Enum.map(input, &parse/1)
    |> Combination.combine(2)
    |> Enum.map(&area/1)
    |> Enum.max()
  end
end
