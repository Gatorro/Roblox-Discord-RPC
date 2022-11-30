if not(game:IsLoaded())then game.Loaded:Wait()end
function checkws()
    ws = syn.websocket.connect("ws://127.0.0.1:8080")
    ws.OnClose:Connect(function()
        game.StarterGui:SetCore("ChatMakeSystemMessage",{Text = "[WebSocket]: Disconnected.",Color = Color3.fromRGB(255,65,65)})
    end)
    ws.OnMessage:Connect(function(msg)
        ChatEvent(msg)
    end)
end
function connect()
    if pcall(checkws) then game.StarterGui:SetCore("ChatMakeSystemMessage",{Text = "[WebSocket]: Connected to 127.0.0.1",Color = Color3.fromRGB(65,255,65)})else game.StarterGui:SetCore("ChatMakeSystemMessage",{Text = "[WebSocket]: Couldn't connect",Color = Color3.fromRGB(255,65,65)})end
end
function richstart()
    task.spawn(function()
        while true do
            local code,error = pcall(function()
                local gameName = game:GetService("MarketplaceService"):GetProductInfo(game.PlaceId)
                ws:Send(gameName.Name..'|'..game.PlaceId)
            end)
            if not code then
                print(error)
                break
            end
            task.wait(6)
        end
    end)
end
connect()
richstart()
local players, replicatedStorage = game:GetService("Players"), game:GetService("ReplicatedStorage");
local defaultChatSystemChatEvents = replicatedStorage:FindFirstChild("DefaultChatSystemChatEvents");
local onMessageDoneFiltering = defaultChatSystemChatEvents:FindFirstChild("OnMessageDoneFiltering");
local prefix = "rpc."
onMessageDoneFiltering.OnClientEvent:Connect(function(messageData)
    local speaker, message = players[messageData.FromSpeaker], messageData.Message
    -- Functions2:
    function addCmd(commandV)
        return string.match(message,"^"..prefix..tostring(commandV))
    end
    -- end
    if speaker.Name == game.Players.LocalPlayer.Name then
        if addCmd("connect") or addCmd("c") then
            connect()
            richstart()
        end                                            
    end
end);
