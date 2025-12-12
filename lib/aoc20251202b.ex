defmodule Aoc20251202b do
  def rep?(i) when i < 10, do: false

  def rep?(i) do
    s = Integer.to_string(i)
    l = String.length(s)

    Enum.any?(2..l, fn n ->
      rem(l, n) == 0 and
        String.slice(s, 0, div(l, n))
        |> String.duplicate(n) == s
    end)
  end

  def calc([a, b], total) do
    Enum.reduce(a..b, total, fn
      i, total -> if rep?(i), do: total + i, else: total
    end)
  end

  def call(input) do
    List.first(input)
    |> String.split(",")
    |> Enum.map(&Aoc20251202a.parse/1)
    |> Enum.reduce(0, &calc/2)
  end
end
