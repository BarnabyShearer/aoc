defmodule Aoc20251204b do
  def count([], _), do: 0
  def count([x | xs], x), do: 1 + count(xs, x)
  def count([_ | xs], x), do: count(xs, x)

  def count(input), do: Enum.reduce(input, 0, fn l, acc -> acc + count(l, "@") end)

  def calc([prev, row, next]) do
    Enum.with_index(row)
    |> Enum.map(fn
      {"@", i} ->
        if Aoc20251204a.accessable?([prev, row, next], i), do: ".", else: "@"

      {".", _i} ->
        "."
    end)
  end

  def call(input) do
    input = Enum.map(input, &Aoc20251204a.parse/1)
    start = count(input)

    input =
      Enum.reduce_while(1..99999, input, fn _, acc ->
        output =
          ([List.duplicate(".", 99999)] ++ acc ++ [List.duplicate(".", 99999)])
          |> Enum.chunk_every(3, 1, :discard)
          |> Enum.map(&calc/1)

        if count(acc) == count(output), do: {:halt, output}, else: {:cont, output}
      end)

    start - count(input)
  end
end
