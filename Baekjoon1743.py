{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Baekjoon1743.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNMjJ/qpqHAqxkZL6IUojBn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/seungyeonseong/Python_PS/blob/main/Baekjoon1743.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import sys\n",
        "from collections import deque\n",
        "input = sys.stdin.readline\n",
        "\n",
        "n, m, k = map(int,input().split())\n",
        "graph= [[0]*m for _ in range(n)]\n",
        "\n",
        "for _ in range(k):\n",
        "    r,c = map(int,input().split())\n",
        "    graph[r-1][c-1] = -1\n",
        "\n",
        "dx = [1,0,-1,0]\n",
        "dy = [0,1,0,-1]\n",
        "\n",
        "def bfs(x,y):\n",
        "    res = 1\n",
        "    q = deque()\n",
        "    q.append((x,y))\n",
        "    graph[x][y] = 1\n",
        "    while q:\n",
        "        x,y = q.popleft()\n",
        "        for i in range(4):\n",
        "            nx = x + dx[i]\n",
        "            ny = y + dy[i]\n",
        "            if nx <0 or nx >=n or ny <0 or ny >=m or graph[nx][ny]==0:\n",
        "                continue\n",
        "            if graph[nx][ny]==-1:\n",
        "                graph[nx][ny] = 1\n",
        "                res += 1\n",
        "                q.append((nx,ny))\n",
        "    return res\n",
        "\n",
        "total = 0\n",
        "for i in range(n):\n",
        "  for j in range(m):\n",
        "    if graph[i][j] == -1:\n",
        "        v = bfs(i,j)\n",
        "        total  = max(total,v)\n",
        "\n",
        "print(total)"
      ],
      "metadata": {
        "id": "ShPsrFxVXa1R"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}