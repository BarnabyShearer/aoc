defmodule Shape do
  def width(cells),
    do: (Enum.map(cells, fn {x, _} -> x end) |> Enum.max()) + 1

  def height(cells),
    do: (Enum.map(cells, fn {_, y} -> y end) |> Enum.max()) + 1

  def rotations(cells) do
    r1 = rotate_90(cells)
    r2 = rotate_90(r1)
    r3 = rotate_90(r2)
    [cells, r1, r2, r3]
  end

  def rotate_90(cells) do
    Enum.map(cells, fn {x, y} -> {y, -x} end)
  end
end

defmodule Space do
  def width(space),
    do: length(hd(space))

  def height(space),
    do: length(space)

  def new(w, h), do: Enum.map(1..h, fn _ -> Enum.map(1..w, fn _ -> false end) end)

  def can_place?(space, cells, x, y) do
    Enum.all?(cells, fn {dx, dy} ->
      gx = x + dx
      gy = y + dy

      gy < height(space) and
        gx < width(space) and
        not (space |> Enum.at(gy) |> Enum.at(gx))
    end)
  end

  def place(space, cells, x, y) do
    Enum.reduce(cells, space, fn {dx, dy}, acc ->
      List.update_at(acc, y + dy, fn row ->
        List.update_at(row, x + dx, fn _ -> true end)
      end)
    end)
  end
end

defmodule Aoc20251212a do
  def fits?(shapes, {width, height}) do
    place_all(
      Enum.flat_map(shapes, fn {shape, count} -> Enum.map(1..count, fn _ -> shape end) end),
      Space.new(width, height),
      %{}
    )
    |> elem(0)
  end

  def place_all([], _space, memo), do: {true, memo}

  def place_all(shapes, space, memo) do
    if Enum.map(shapes, fn s -> length(s) end) |> Enum.sum() >
         List.flatten(space) |> Enum.count(fn g -> !g end) do
      {false, memo}
    else
      key = {space, shapes}

      case memo do
        %{^key => result} ->
          {result, memo}

        _ ->
          [shape | rest] = shapes

          {found, memo2} =
            try_rotations(shape, rest, space, memo)

          memo_final = Map.put(memo2, key, found)
          {found, memo_final}
      end
    end
  end

  def try_rotations(shape, rest, space, memo) do
    Enum.reduce_while(Shape.rotations(shape), {false, memo}, fn rotated, {_, memo_acc} ->
      case try_positions(rotated, rest, space, memo_acc) do
        {true, memo_next} -> {:halt, {true, memo_next}}
        {false, memo_next} -> {:cont, {false, memo_next}}
      end
    end)
  end

  def try_positions(shape, rest, space, memo) do
    Enum.reduce_while(0..(Space.width(space) - Shape.width(shape)), {false, memo}, fn x,
                                                                                      {_, memo_x} ->
      Enum.reduce_while(0..(Space.height(space) - Shape.height(shape)), {false, memo_x}, fn y,
                                                                                            {_,
                                                                                             memo_y} ->
        if Space.can_place?(space, shape, x, y) do
          new_space = Space.place(space, shape, x, y)
          {ok, memo_next} = place_all(rest, new_space, memo_y)

          if ok do
            {:halt, {true, memo_next}}
          else
            {:cont, {false, memo_next}}
          end
        else
          {:cont, {false, memo_y}}
        end
      end)
      |> case do
        {true, _} = res -> {:halt, res}
        {false, _} = res -> {:cont, res}
      end
    end)
  end

  def call(input) do
    shapes =
      Enum.filter(input, fn l -> String.contains?(l, "#") end)
      |> Enum.chunk_every(3)
      |> Enum.map(fn s ->
        Enum.with_index(s)
        |> Enum.flat_map(fn {row, y} ->
          String.graphemes(row)
          |> Enum.with_index()
          |> Enum.filter(fn
            {"#", _} -> true
            _ -> false
          end)
          |> Enum.map(fn {_, x} -> {x, y} end)
        end)
      end)

    Enum.filter(input, fn l -> String.contains?(l, "x") end)
    |> Enum.map(fn l ->
      [w, h | rest] =
        Regex.scan(~r/\d+/, l)
        |> Enum.map(fn [i] -> String.to_integer(i) end)

      {{w, h}, rest}
    end)
    |> Enum.filter(fn {space, nums} ->
      fits?(Enum.zip(shapes, nums), space)
    end)
    |> Enum.count()
  end
end
