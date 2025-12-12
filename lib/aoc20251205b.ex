defmodule Aoc20251205b do
  def call(input) do
    Aoc20251205a.merge(Enum.reduce(input, [], &Aoc20251205a.parse_range/2))
    |> Enum.reduce(0, fn r, acc -> acc + (r.last - r.first + 1) end)
  end
end
