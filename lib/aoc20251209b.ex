defmodule Aoc20251209b do
  def scanlines(nodes) do
    {y_min, y_max} = Enum.map(nodes, fn {_, y} -> y end) |> Enum.min_max()

    Enum.map(y_min..y_max, fn y ->
      {y,
       Enum.zip(nodes, tl(nodes) ++ [hd(nodes)])
       |> Enum.flat_map(fn {{x1, y1}, {x2, y2}} ->
         cond do
           y1 == y2 ->
             []

           y >= min(y1, y2) and y < max(y1, y2) ->
             [x1 + floor((y - y1) * (x2 - x1) / (y2 - y1))]

           true ->
             []
         end
       end)
       |> Enum.sort()
       |> Enum.uniq()
       |> Enum.chunk_every(2)
       |> Enum.map(fn [x1, x2] -> x1..x2 end)}
    end)
  end

  def valid(scanlines, {{x1, y1}, {x2, y2}}) when x1 > x2,
    do: valid(scanlines, {{x2, y1}, {x1, y2}})

  def valid(scanlines, {{x1, y1}, {x2, y2}}) when y1 > y2,
    do: valid(scanlines, {{x1, y2}, {x2, y1}})

  def valid(scanlines, {{x1, y1}, {x2, y2}}) do
    Enum.reduce_while(scanlines, true, fn {y, runs}, _ ->
      if(y < y1 or y > y2 or Enum.any?(runs, fn s..e//_ -> s <= x1 and e >= x2 end),
        do: {:cont, true},
        else: {:halt, false}
      )
    end)
  end

  def call(input) do
    nodes = Enum.map(input, &Aoc20251209a.parse/1)
    scanlines = scanlines(nodes)

    Combination.combine(nodes, 2)
    |> Enum.reduce(0, fn [a, b], acc ->
      next = Aoc20251209a.area([a, b])
      if next > acc and valid(scanlines, {a, b}), do: next, else: acc
    end)
  end
end
