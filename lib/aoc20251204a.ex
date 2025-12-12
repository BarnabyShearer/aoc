defmodule Aoc20251204a do
  def parse(line), do: ["."] ++ String.split(line, "", trim: true) ++ ["."]

  def accessable?([prev, row, next], i),
    do:
      String.count(
        [
          [prev, i - 1],
          [prev, i],
          [prev, i + 1],
          [row, i - 1],
          [row, i + 1],
          [next, i - 1],
          [next, i],
          [next, i + 1]
        ]
        |> Enum.reduce("", fn [r, j], s -> s <> Enum.at(r, j) end),
        "@"
      ) < 4

  def calc([prev, row, next], total) do
    Enum.with_index(row)
    |> Enum.reduce(total, fn
      {"@", i}, acc ->
        acc +
          if accessable?([prev, row, next], i), do: 1, else: 0

      {".", _i}, acc ->
        acc
    end)
  end

  def call(input) do
    ([String.duplicate(".", 99999)] ++ input ++ [String.duplicate(".", 99999)])
    |> Enum.map(&parse/1)
    |> Enum.chunk_every(3, 1, :discard)
    |> Enum.reduce(0, &calc/2)
  end
end
