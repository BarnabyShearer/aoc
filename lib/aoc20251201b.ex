defmodule Aoc20251201b do
  def calc({dir, len}, {pos, count}) do
    on_zero = pos == 0
    pos = pos + if(dir == :right, do: len, else: -len)
    count = count + div(abs(pos), 100) + if pos < 1 and not on_zero, do: 1, else: 0
    pos = Integer.mod(pos, 100)
    {pos, count}
  end

  def call(input) do
    Enum.map(input, &Aoc20251201a.parse/1)
    |> Enum.reduce({50, 0}, &calc/2)
    |> elem(1)
  end
end
