defmodule Aoc20251203b do
  def call(input) do
    Enum.map(input, &Aoc20251203a.parse/1)
    |> Enum.reduce({0, 12}, &Aoc20251203a.calc/2)
    |> elem(0)
  end
end
