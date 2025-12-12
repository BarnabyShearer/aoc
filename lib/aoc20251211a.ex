defmodule Aoc20251211a do
  def parse(line), do: String.split(line, " ", trim: true)

  def dfs(_graph, current, target, path, paths) when current == target,
    do: [Enum.reverse([current | path]) | paths]

  def dfs(graph, current, target, path, paths) do
    neighbors = Map.get(graph, current, [])

    Enum.reduce(neighbors, paths, fn neighbor, acc ->
      if neighbor in path do
        acc
      else
        dfs(graph, neighbor, target, [current | path], acc)
      end
    end)
  end

  def call(input) do
    Enum.map(input, &parse/1)
    |> Map.new(fn [head | tail] -> {String.slice(head, 0..(String.length(head) - 2)), tail} end)
    |> dfs("you", "out", [], [])
    |> Enum.count()
  end
end
