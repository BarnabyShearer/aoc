defmodule Aoc20251206a do
  def parse(<<"+", line::binary>>), do: ["+"] ++ String.split(line, " ", trim: true)
  def parse(<<"*", line::binary>>), do: ["*"] ++ String.split(line, " ", trim: true)
  def parse(line), do: String.split(line, " ", trim: true) |> Enum.map(&String.to_integer/1)

  def call(input) do
    [opp | data] = Enum.map(input, &parse/1) |> Enum.reverse()

    Enum.with_index(opp)
    |> Enum.map(fn
      {"+", i} -> Enum.map(data, fn l -> Enum.at(l, i) end) |> Enum.sum()
      {"*", i} -> Enum.map(data, fn l -> Enum.at(l, i) end) |> Enum.product()
    end)
    |> Enum.sum()
  end
end
