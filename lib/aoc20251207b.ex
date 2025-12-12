defmodule Aoc20251207b do
  def call(input) do
    [start | data] = input
    start = String.graphemes(start) |> Enum.find_index(fn c -> c == "S" end)

    Enum.reduce(data, %{start => 1}, fn line, b ->
      Enum.reduce(Map.keys(b), b, fn i, b ->
        if String.at(line, i) == "^" do
          next = Map.put(b, i, 0)
          next = Map.put(next, i - 1, Map.get(b, i - 1, 0) + Map.get(b, i, 0))
          Map.put(next, i + 1, Map.get(b, i + 1, 0) + Map.get(b, i, 0))
        else
          b
        end
      end)
    end)
    |> Map.values()
    |> Enum.sum()
  end
end
