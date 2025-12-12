defmodule Aoc20251208b do
  def call(input) do
    nodes = Enum.map(input, &Aoc20251208a.parse/1)
    node_count = Enum.count(nodes)

    Aoc20251208a.by_distance(nodes)
    |> Enum.reduce_while([], fn [a, b], acc ->
      circits = Aoc20251208a.circits([a, b], acc)

      if MapSet.size(Enum.at(circits, 0)) == node_count do
        {:halt, Enum.at(a, 0) * Enum.at(b, 0)}
      else
        {:cont, circits}
      end
    end)
  end
end
