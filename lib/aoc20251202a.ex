defmodule Aoc20251202a do
  def parse(line), do: String.split(line, "-") |> Enum.map(&String.to_integer/1)

  def rep?(i) do
    s = Integer.to_string(i)
    l = String.length(s)
    lh = div(l, 2)
    String.slice(s, 0, lh) == String.slice(s, lh, l - lh)
  end

  def calc([a, b], total) do
    Enum.reduce(a..b, total, fn
      i, total -> if rep?(i), do: total + i, else: total
    end)
  end

  def call(input) do
    List.first(input)
    |> String.split(",")
    |> Enum.map(&parse/1)
    |> Enum.reduce(0, &calc/2)
  end
end
