defmodule Aoc20251208a do
  def parse(line), do: String.split(line, ",") |> Enum.map(&String.to_integer/1)

  def distance([x1, y1, z1], [x2, y2, z2]),
    do: ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

  def circits([a, b], acc) do
    case {
      Enum.find_index(acc, fn l -> MapSet.member?(l, a) end),
      Enum.find_index(acc, fn l -> MapSet.member?(l, b) end)
    } do
      {nil, nil} ->
        acc ++ [MapSet.new([a, b])]

      {ai, nil} ->
        List.update_at(acc, ai, fn s -> MapSet.put(s, b) end)

      {nil, bi} ->
        List.update_at(acc, bi, fn s -> MapSet.put(s, a) end)

      {ai, bi} ->
        if ai == bi do
          acc
        else
          List.delete_at(
            List.update_at(acc, ai, fn s -> MapSet.union(s, Enum.at(acc, bi)) end),
            bi
          )
        end
    end
  end

  def by_distance(nodes),
    do:
      Combination.combine(nodes, 2)
      |> Enum.sort(fn [a1, b1], [a2, b2] -> distance(a1, b1) <= distance(a2, b2) end)

  def call(input) do
    Enum.map(input, &parse/1)
    |> by_distance()
    |> Enum.slice(0..999)
    |> Enum.reduce([], &circits/2)
    |> Enum.map(&MapSet.size/1)
    |> Enum.sort()
    |> Enum.slice(-3..-1)
    |> Enum.product()
  end
end
