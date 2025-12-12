defmodule Aoc20251205a do
  def parse_range(line, acc) do
    if String.contains?(line, "-") do
      acc ++
        [
          String.split(line, "-")
          |> Enum.map(&String.to_integer/1)
          |> (fn [a, b] -> a..b end).()
        ]
    else
      acc
    end
  end

  def parse_numbers(line, acc) do
    if String.contains?(line, "-") do
      acc
    else
      acc ++ [String.to_integer(line)]
    end
  end

  def min_first(a, b), do: a.first <= b.first

  def cons(new, [head | tail])
      when head.last >= new.first, do: [head.first..max(head.last, new.last) | tail]

  def cons(new, rest),
    do: [new | rest]

  def prep([]), do: []
  def prep([head | tail]), do: [[head] | tail]

  def merge(all) do
    Enum.sort(all, &min_first/2)
    |> prep()
    |> Enum.reduce(&cons/2)
    |> Enum.reverse()
  end

  def call(input) do
    ranges = merge(Enum.reduce(input, [], &parse_range/2))

    Enum.reduce(input, [], &parse_numbers/2)
    |> Enum.reduce(0, fn n, acc ->
      if Enum.any?(ranges, fn r -> n in r end) do
        acc + 1
      else
        acc
      end
    end)
  end
end
