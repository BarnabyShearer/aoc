defmodule Aoc20251207a do
  def call(input) do
    [start | data] = input
    start = String.graphemes(start) |> Enum.find_index(fn c -> c == "S" end)

    Enum.reduce(data, {0, MapSet.new([start])}, fn line, {t, b} ->
      Enum.reduce(b, {t, b}, fn i, {t, b} ->
        if String.at(line, i) == "^" do
          next = MapSet.delete(b, i)
          next = MapSet.put(next, i - 1)
          next = MapSet.put(next, i + 1)
          {t + 1, next}
        else
          {t, b}
        end
      end)
    end)
    |> elem(0)
  end
end
