defmodule Aoc20251206b do
  def blank?(l), do: Enum.all?(l, fn i -> i == " " end)

  def call(input) do
    Enum.map(input, &String.graphemes/1)
    |> Enum.zip_with(&Function.identity/1)
    |> Enum.chunk_by(&blank?/1)
    |> Enum.reject(fn l -> blank?(Enum.at(l, 0)) end)
    |> Enum.map(fn l ->
      {Enum.at(Enum.at(l, 0), -1),
       Enum.map(l, fn ll ->
         String.to_integer(String.trim(Enum.join(List.pop_at(ll, -1) |> elem(1))))
       end)}
    end)
    |> Enum.map(fn
      {"+", i} -> Enum.sum(i)
      {"*", i} -> Enum.product(i)
    end)
    |> Enum.sum()
  end
end
