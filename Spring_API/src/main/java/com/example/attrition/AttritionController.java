package com.example.attrition;

import lombok.RequiredArgsConstructor;
import org.jetbrains.annotations.NotNull;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
@RequestMapping("api/")
public class AttritionController {

    private final AttritionService attritionService;

    @PostMapping("/register")
    public void register(@RequestBody HumanResources humanResources){
        attritionService.register(humanResources);
    }

    @PostMapping("/login")
    public boolean login(@RequestBody @NotNull LoginRequest loginRequest){
        return attritionService.validation(loginRequest.getEmail(), loginRequest.getPassword());
    }
}
