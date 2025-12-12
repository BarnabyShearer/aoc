defmodule Aoc20251201a do
  def parse(<<"R", rest::binary>>), do: {:right, String.to_integer(rest)}
  def parse(<<"L", rest::binary>>), do: {:left, String.to_integer(rest)}

  def calc({dir, len}, {pos, count}) do
    pos = rem(pos + if(dir == :right, do: len, else: -len), 100)
    {pos, count + if(pos == 0, do: 1, else: 0)}
  end

  def call(input) do
    Enum.map(input, &parse/1)
    |> Enum.reduce({50, 0}, &calc/2)
    |> elem(1)
  end
end
